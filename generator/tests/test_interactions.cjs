// Deterministic controller tests: DOM stubs exercise failure and lifecycle paths
// that complement the real-browser interaction checks.
const fs = require('node:fs');
const vm = require('node:vm');
const assert = require('node:assert/strict');
const path = require('node:path');
const source = fs.readFileSync(path.join(__dirname,'../templates/scripts.py'),'utf8').split("INTERACTION_SCRIPT = r'''")[1].split("'''")[0];
class Node {
  constructor(name='') { this.name=name; this.listeners={}; this.attrs={}; this.dataset={}; this.style={setProperty(k,v){this[k]=v},removeProperty(k){delete this[k]}}; this.hidden=false; this.textContent=''; this.queries={}; this.lists={}; this.classes=new Set(); this.classList={add:(x)=>this.classes.add(x),remove:(x)=>this.classes.delete(x),toggle:(x,b)=>b?this.classes.add(x):this.classes.delete(x)}; }
  addEventListener(name,fn) { (this.listeners[name]??=[]).push(fn); }
  fire(name,event={}) { for(const fn of this.listeners[name]??[]) fn(event); }
  appendChild(node) { (this.children??=[]).push(node); }
  getBoundingClientRect() { return {top:0,height:100,width:400}; }
  querySelector(q) { return this.queries[q]??null; }
  querySelectorAll(q) { return this.lists[q]??[]; }
  setAttribute(k,v) { this.attrs[k]=v; }
  getAttribute(k) { return this.attrs[k]; }
  closest() { return this.sceneRoot??null; }
  contains(n) { return n===this; }
  animate(frames,options) { const a={frames,options,state:'running',pause(){this.state='paused'},play(){this.state='running'},cancel(){this.state='cancelled'}}; this.lastAnimation=a; return a; }
}
function setup({systemReduced=false,storageFails=false,scene=null}={}) {
  const doc=new Node('document');doc.createElement=()=>new Node();doc.documentElement=new Node('root');doc.body=new Node('body');doc.hidden=false;doc.activeElement=null;
  const toggle=new Node('motion');const chapter=new Node('chapter');const carousel=new Node('carousel');const pause=new Node('pause');const prev=new Node('prev');const next=new Node('next');const position=new Node('position');const status=new Node('status');const gallery=new Node('gallery');
  const slides=Array.from({length:3},(_,i)=>{const n=new Node('slide'+i);n.queries.figcaption=new Node();n.queries.figcaption.textContent='Screen '+(i+1);return n});
  const dots=slides.map((_,i)=>{const n=new Node('dot'+i);n.dataset.slide=String(i);return n});
  carousel.queries={'.carousel-pause':pause,'.carousel-prev':prev,'.carousel-next':next,'.carousel-position':position,'.carousel-status':status,'.meme-arcade-gallery':gallery,'.carousel-controls':new Node()};
  carousel.lists={'.meme-arcade-screen-card':slides,'.carousel-dot':dots};
  doc.queries['.meme-carousel']=carousel;
  doc.lists['main > section']=[chapter];
  if(scene){chapter.sceneRoot=chapter;doc.lists[scene]=[chapter]}
  doc.getElementById=id=>id==='motion-toggle'?toggle:null;
  const queries=new Map();function matchMedia(q){if(!queries.has(q)){const m=new Node(q);m.matches=q.includes('prefers-reduced')?systemReduced:q.includes('hover: hover');queries.set(q,m)}return queries.get(q)}
  const observers=[];class IO{constructor(callback){this.callback=callback;this.targets=new Set();observers.push(this)}observe(el){this.targets.add(el)}unobserve(el){this.targets.delete(el)}disconnect(){this.targets.clear()}}
  const timers=new Map();let timerID=0;
  const win=new Node('window');win.IntersectionObserver=IO;win.scrollY=0;win.innerHeight=900;const frames=new Map();let frameID=0;
  let time=0;
  const context={performance:{now:()=>time},document:doc,window:win,Element:Node,IntersectionObserver:IO,matchMedia,localStorage:{getItem(){if(storageFails)throw Error('blocked');return null},setItem(){if(storageFails)throw Error('blocked')}},location:{hash:'',pathname:'/',replace(){}},URL,navigator:{},requestAnimationFrame:fn=>{frames.set(++frameID,fn);return frameID},cancelAnimationFrame:id=>frames.delete(id),setTimeout:(fn,ms)=>{timers.set(++timerID,{fn,ms});return timerID},clearTimeout:id=>timers.delete(id),console};
  vm.runInNewContext(source,context);
  function visible(el,state){for(const o of observers)if(o.targets.has(el))o.callback([{target:el,isIntersecting:state}])}
  return {doc,toggle,chapter,carousel,pause,prev,next,position,status,slides,dots,timers,queries,visible,win,frames,advance(ms){time+=ms},flush(){const pending=[...frames.values()];frames.clear();pending.forEach(fn=>fn())}};
}
const tests=[];function test(name,fn){fn();tests.push(name);console.log('PASS',name)}
test('Autoplay waits for visibility, advances every 3000ms, and stops on interaction',()=>{
 const t=setup();assert.equal(t.timers.size,0);t.visible(t.carousel,true);assert.equal(t.carousel.dataset.autoplay,'playing');assert.equal([...t.timers.values()][0].ms,3000);
 [...t.timers.values()][0].fn();assert.equal(t.position.textContent,'2 / 3');assert.equal(t.slides.filter(s=>!s.hidden).length,1);
 t.carousel.fire('pointerdown');assert.equal(t.timers.size,0);assert.equal(t.carousel.dataset.autoplay,'paused');
 t.visible(t.carousel,false);t.visible(t.carousel,true);assert.equal(t.timers.size,0);
 t.next.fire('click');assert.equal(t.position.textContent,'3 / 3');t.next.fire('click');assert.equal(t.position.textContent,'1 / 3');assert.equal(t.timers.size,0);
});
test('Pause remains paused despite focusin; explicit Play restarts',()=>{
 const t=setup();t.visible(t.carousel,true);t.pause.fire('pointerdown');t.carousel.fire('pointerdown');t.carousel.fire('focusin');t.pause.fire('click');assert.equal(t.timers.size,0);
 t.pause.fire('pointerdown');t.carousel.fire('pointerdown');t.pause.fire('click');assert.equal(t.carousel.dataset.autoplay,'playing');assert.equal(t.timers.size,1);
});
test('Hidden tab and offscreen clear timers, returning starts a fresh interval',()=>{
 const t=setup();t.visible(t.carousel,true);t.doc.hidden=true;t.doc.fire('visibilitychange');assert.equal(t.timers.size,0);
 t.doc.hidden=false;t.doc.fire('visibilitychange');assert.equal(t.timers.size,1);t.visible(t.carousel,false);assert.equal(t.timers.size,0);
});
test('Reduced motion disables auto but preserves manual slide navigation',()=>{
 const t=setup({systemReduced:true});t.visible(t.carousel,true);t.visible(t.chapter,true);assert.equal(t.timers.size,0);assert.equal(t.chapter.lastAnimation,undefined);assert.equal(t.pause.disabled,true);
 t.next.fire('click');assert.equal(t.position.textContent,'2 / 3');assert.equal(t.timers.size,0);
});
test('Storage failures do not break toggle or canceling an active entrance',()=>{
 const t=setup({storageFails:true});t.visible(t.chapter,true);assert.equal(t.chapter.lastAnimation.state,'running');t.toggle.fire('click');assert.equal(t.doc.documentElement.dataset.reducedMotion,'true');assert.equal(t.chapter.lastAnimation.state,'cancelled');
});
test('Offscreen entrances pause and complete without retaining transforms',()=>{
 const t=setup();t.visible(t.chapter,true);const animation=t.chapter.lastAnimation;t.visible(t.chapter,false);assert.equal(animation.state,'paused');t.visible(t.chapter,true);assert.equal(animation.state,'running');animation.onfinish();assert.equal(animation.state,'cancelled');
});
test('Keyboard pagination announces a stable selected slide and stops autoplay',()=>{
 const t=setup();t.visible(t.carousel,true);let prevented=false;t.carousel.fire('keydown',{key:'ArrowRight',preventDefault(){prevented=true}});assert.equal(prevented,true);assert.equal(t.position.textContent,'2 / 3');assert.match(t.status.textContent,/Screen 2/);assert.equal(t.dots[1].attrs['aria-current'],'true');assert.equal(t.timers.size,0);
});
test('Desktop scroll parallax is bounded, coalesced, and disabled on mobile',()=>{
 const t=setup();t.visible(t.chapter,true);t.flush();assert.equal(t.chapter.style['--scroll-depth-y'],'19.20px');
 t.win.scrollY=1000;t.win.fire('scroll');t.win.fire('scroll');assert.equal(t.frames.size,1);t.flush();assert.equal(t.chapter.style['--scroll-depth-y'],'24.00px');assert.equal(t.frames.size,0);
 const compact=t.queries.get('(max-width: 800px)');compact.matches=true;compact.fire('change');assert.equal(t.chapter.lastAnimation.state,'cancelled');assert.equal(t.chapter.style['--scroll-depth-y'],undefined);t.win.fire('scroll');assert.equal(t.frames.size,0);
});
test('Sustained slow requested frames simplify depth, then retain a static visit',()=>{
 const t=setup();t.visible(t.chapter,true);t.visible(t.carousel,true);
 for(let i=0;i<20;i++){t.win.fire('scroll');t.advance(60);t.flush()}
 assert.equal(t.doc.documentElement.dataset.motionQuality,'calm');
 for(let i=0;i<20;i++){t.win.fire('scroll');t.advance(60);t.flush()}
 assert.equal(t.doc.documentElement.dataset.motionQuality,'static');assert.equal(t.doc.documentElement.dataset.reducedMotion,'true');assert.equal(t.timers.size,0);assert.equal(t.frames.size,0);
 t.win.fire('scroll');assert.equal(t.frames.size,0);t.next.fire('click');assert.equal(t.position.textContent,'2 / 3');
});
test('Rows receive distinct identities while interactive chapter geometry stays fixed',()=>{
 const memory=setup({scene:'#clineflow'}), arcade=setup({scene:'#memearcade'}), film=setup({scene:'#filmography'});
 for(const t of [memory,arcade,film]){t.visible(t.chapter,true);assert.ok(t.chapter.lastAnimation.frames.every(frame=>!('transform' in frame)));assert.equal(t.chapter.children[0].attrs['aria-hidden'],'true')}
 assert.equal(memory.chapter.dataset.transition,'memory-flow');assert.equal(arcade.chapter.dataset.transition,'arcade-pop');assert.equal(film.chapter.dataset.transition,'cinema-curtain');
 assert.equal(memory.chapter.style['--scene-animation'],'scene-scan');assert.equal(arcade.chapter.style['--scene-animation'],'scene-prism');assert.equal(film.chapter.style['--scene-animation'],'scene-curtain');
 memory.doc.hidden=true;memory.doc.fire('visibilitychange');assert.equal(memory.chapter.lastAnimation.state,'paused');memory.toggle.fire('click');assert.equal(memory.chapter.lastAnimation.state,'cancelled');
});
console.log(`${tests.length} controller tests passed.`);
