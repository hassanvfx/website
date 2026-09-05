(()=>{
 const samples=[]; let last=0, cls=0;
 let layoutObserver;
 try { layoutObserver=new PerformanceObserver(list=>{for(const e of list.getEntries())if(!e.hadRecentInput)cls+=e.value});layoutObserver.observe({type:'layout-shift',buffered:true}); } catch(_) {}
 function tick(now){if(last)samples.push(now-last);last=now;if(samples.length<179)requestAnimationFrame(tick);else{
  const sorted=[...samples].sort((a,b)=>a-b);const resources=performance.getEntriesByType('resource');
  const result={width:innerWidth,height:innerHeight,dpr:devicePixelRatio,frames:samples.length,meanIntervalMs:samples.reduce((a,b)=>a+b,0)/samples.length,p95IntervalMs:sorted[Math.floor(sorted.length*.95)],intervalsAbove50ms:samples.filter(x=>x>50).length,layoutShiftSupported:!!layoutObserver,observedCLS:cls,topFrameResourceTransfer:resources.reduce((s,r)=>s+r.transferSize,0),topFrameResourceCount:resources.length,navigationDuration:performance.getEntriesByType('navigation')[0]?.duration};
  const output=document.createElement('output');output.id='qa-metrics';output.hidden=true;output.textContent=JSON.stringify(result);document.body.append(output);layoutObserver?.disconnect();
 }}requestAnimationFrame(tick);
})();
