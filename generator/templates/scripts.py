"""Shared progressive enhancement for the generated portfolio."""

RESUME_SCRIPT = r'''

    const viewer = document.querySelector('.professional-profile-viewer');
    if ('IntersectionObserver' in window) {
      await new Promise(resolve => {
        const observer = new IntersectionObserver(entries => {
          if (entries.some(entry => entry.isIntersecting)) { observer.disconnect(); resolve(); }
        }, { rootMargin: '250px' });
        observer.observe(viewer);
      });
    }
    let pdfjsLib;

    const resumeUrl = document.querySelector('.professional-profile-download').getAttribute('href');
    const resumeCanvas = document.getElementById('resumeCanvas');
    const resumePreview = document.getElementById('resumePreview');
    const resumeCanvasWrap = document.getElementById('resumeCanvasWrap');
    const resumeStatus = document.getElementById('resumeStatus');
    const resumePageIndicator = document.getElementById('resumePageIndicator');
    const resumePrevious = document.getElementById('resumePrevious');
    const resumeNext = document.getElementById('resumeNext');
    const resumeZoomOut = document.getElementById('resumeZoomOut');
    const resumeZoomIn = document.getElementById('resumeZoomIn');

    let resumePdf = null;
    let resumePage = 1;
    let resumeZoom = 1;
    let resumeRenderTask = null;



    function updateResumeControls() {
      const ready = Boolean(resumePdf);
      resumePrevious.disabled = !ready || resumePage <= 1;
      resumeNext.disabled = !ready || resumePage >= resumePdf.numPages;
      resumeZoomOut.disabled = !ready || resumeZoom <= 0.75;
      resumeZoomIn.disabled = !ready || resumeZoom >= 1.75;
      if (ready) {
        resumePageIndicator.textContent = `${resumePage} / ${resumePdf.numPages}`;
      }
    }

    async function renderResumePage() {
      if (!resumePdf) return;
      if (resumeRenderTask) {
        resumeRenderTask.cancel();
      }
      resumeStatus.textContent = `Rendering page ${resumePage}…`;
      const page = await resumePdf.getPage(resumePage);
      const baseViewport = page.getViewport({ scale: 1 });
      const viewerPadding = window.matchMedia('(max-width: 768px)').matches ? 16 : 32;
      const availableWidth = Math.max(1, resumeCanvasWrap.clientWidth - viewerPadding);
      const fitScale = Math.min(1, availableWidth / baseViewport.width);
      const viewport = page.getViewport({ scale: fitScale * resumeZoom });
      const outputScale = window.devicePixelRatio || 1;
      const context = resumeCanvas.getContext('2d', { alpha: false });
      resumeCanvas.width = Math.floor(viewport.width * outputScale);
      resumeCanvas.height = Math.floor(viewport.height * outputScale);
      resumeCanvas.style.width = `${Math.floor(viewport.width)}px`;
      resumeCanvas.style.height = `${Math.floor(viewport.height)}px`;
      resumeRenderTask = page.render({
        canvasContext: context,
        viewport,
        transform: outputScale !== 1 ? [outputScale, 0, 0, outputScale, 0, 0] : null,
      });
      try {
        await resumeRenderTask.promise;
        resumeStatus.textContent = `Resume page ${resumePage} of ${resumePdf.numPages}`;
      } catch (error) {
        if (error?.name !== 'RenderingCancelledException') {
          throw error;
        }
      } finally {
        resumeRenderTask = null;
      }
      updateResumeControls();
    }

    try {
      pdfjsLib = await import('https://cdn.jsdelivr.net/npm/pdfjs-dist@5.3.31/build/pdf.mjs');
      pdfjsLib.GlobalWorkerOptions.workerSrc = 'https://cdn.jsdelivr.net/npm/pdfjs-dist@5.3.31/build/pdf.worker.mjs';
      const loadingTask = pdfjsLib.getDocument(resumeUrl);
      resumePdf = await loadingTask.promise;
      resumeCanvas.hidden = false;
      await renderResumePage();
      resumePreview.hidden = true;
      updateResumeControls();
    } catch (error) {
      console.error('Unable to load embedded resume:', error);
      resumeCanvas.hidden = true;
      resumePreview.hidden = false;
      resumeStatus.textContent = 'Preview available — use the PDF link for the full resume.';
    }

    resumePrevious.addEventListener('click', async () => {
      if (resumePage > 1) {
        resumePage -= 1;
        await renderResumePage();
      }
    });
    resumeNext.addEventListener('click', async () => {
      if (resumePdf && resumePage < resumePdf.numPages) {
        resumePage += 1;
        await renderResumePage();
      }
    });
    resumeZoomOut.addEventListener('click', async () => {
      resumeZoom = Math.max(0.75, resumeZoom - 0.25);
      await renderResumePage();
    });
    resumeZoomIn.addEventListener('click', async () => {
      resumeZoom = Math.min(1.75, resumeZoom + 0.25);
      await renderResumePage();
    });

    let resumeResizeTimer;
    window.addEventListener('resize', () => {
      if (!resumePdf) return;
      window.clearTimeout(resumeResizeTimer);
      resumeResizeTimer = window.setTimeout(() => renderResumePage(), 150);
    });

'''

INTERACTION_SCRIPT = r'''
(() => {
  'use strict';
  const root = document.documentElement;
  // A second script execution must not install observers, listeners, or layers again.
  if (root.dataset.signalInitialized === 'true') return;
  root.dataset.signalInitialized = 'true';
  const header = document.querySelector('.site-header');
  const measureHeader = () => {
    if (header) root.style.setProperty('--header-clearance', `${Math.ceil(header.getBoundingClientRect().height)}px`);
  };
  measureHeader();
  if (header && 'ResizeObserver' in window) new ResizeObserver(measureHeader).observe(header);
  else window.addEventListener('resize', measureHeader);
  const reducedQuery = matchMedia('(prefers-reduced-motion: reduce)');
  const compactQuery = matchMedia('(max-width: 800px)');
  const fineQuery = matchMedia('(hover: hover) and (pointer: fine)');
  const menu = document.getElementById('mobileMenu');
  const menuButton = document.querySelector('.menu-toggle');
  const motionButton = document.getElementById('motion-toggle');
  let manualReduced = false;
  try { manualReduced = localStorage.getItem('signal-reduce-motion') === 'true'; } catch (_) {}
  let reduced = false;
  let performanceReduced = false;
  let depthQuality = 1;
  let frameQueuedAt = 0;
  let frameSamples = [];
  let menuOpen = false;
  let previousOverflow = '';
  const animations = new Map();
  const playbackSubscribers = [];
  let pointerFrame = 0;
  let pointer = { x: 0, y: 0 };
  const stage = document.querySelector('.portrait-stage');
  const rig = document.querySelector('.depth-rig');
  let stageRect = null;
  let stageVisible = false;
  const stopped = () => reduced || document.hidden || menuOpen;

  function resetDepth() {
    cancelAnimationFrame(pointerFrame); pointerFrame = 0;
    if (rig) { rig.style.removeProperty('--tilt-x'); rig.style.removeProperty('--tilt-y'); }
  }
  function syncPlayback() {
    for (const [element, record] of animations) {
      element.classList.toggle('motion-offscreen', !record.visible);
      if (stopped() || !record.visible) record.animation.pause();
      else record.animation.play();
    }
    root.dataset.motionState = reduced ? 'reduced' : (document.hidden || menuOpen ? 'paused' : 'ready');
    if (stopped()) resetDepth();
    playbackSubscribers.forEach(update => update());
  }
  function syncMotion() {
    reduced = reducedQuery.matches || manualReduced || performanceReduced;
    root.dataset.reducedMotion = String(reduced);
    if (motionButton) {
      motionButton.hidden = false;
      motionButton.setAttribute('aria-pressed', String(reduced));
      motionButton.textContent = performanceReduced ? 'Reduced motion · performance' : (reducedQuery.matches ? 'Reduced motion · system preference' : (manualReduced ? 'Enable animations' : 'Reduce motion'));
      motionButton.disabled = reducedQuery.matches || performanceReduced;
    }
    if (reduced) {
      for (const element of animations.keys()) finishEntrance(element);
    }
    syncPlayback();
  }
  motionButton?.addEventListener('click', () => {
    manualReduced = !manualReduced;
    try { localStorage.setItem('signal-reduce-motion', String(manualReduced)); } catch (_) {}
    syncMotion();
  });
  reducedQuery.addEventListener('change', syncMotion);
  document.addEventListener('visibilitychange', syncPlayback);
  syncMotion();

  // A native modal keeps keyboard focus and background content separate.
  function closeMenu(restoreFocus = true) {
    if (!menuOpen) return;
    menuOpen = false;
    menu.close();
    document.body.style.overflow = previousOverflow;
    menuButton.setAttribute('aria-expanded', 'false');
    syncPlayback();
    if (restoreFocus) {
      if (compactQuery.matches) menuButton.focus({ preventScroll: true });
      else document.querySelector('.site-identity')?.focus({ preventScroll: true });
    }
  }
  if (menu && menuButton && typeof menu.showModal === 'function') {
    menuButton.hidden = false;
    menuButton.addEventListener('click', () => {
      previousOverflow = document.body.style.overflow;
      menuOpen = true; menu.showModal();
      document.body.style.overflow = 'hidden';
      menuButton.setAttribute('aria-expanded', 'true');
      menu.querySelector('.menu-close').focus(); syncPlayback();
    });
    menu.querySelector('.menu-close').addEventListener('click', () => closeMenu());
    menu.addEventListener('cancel', event => { event.preventDefault(); closeMenu(); });
    menu.addEventListener('keydown', event => {
      if (event.key !== 'Tab') return;
      const items = [...menu.querySelectorAll('a[href], button:not([disabled])')];
      const first = items[0], last = items[items.length - 1];
      if (event.shiftKey && document.activeElement === first) { event.preventDefault(); last.focus(); }
      else if (!event.shiftKey && document.activeElement === last) { event.preventDefault(); first.focus(); }
    });
    menu.querySelectorAll('a').forEach(link => link.addEventListener('click', () => {
      const url = new URL(link.href);
      closeMenu(false);
      if (url.pathname === location.pathname && url.hash) {
        const target = document.getElementById(decodeURIComponent(url.hash.slice(1)));
        if (target) { target.setAttribute('tabindex', '-1'); target.focus({ preventScroll: true }); }
      } else menuButton.focus({ preventScroll: true });
    }));
    compactQuery.addEventListener('change', () => { if (!compactQuery.matches) closeMenu(); resetDepth(); });
  }

  // Preserve old inbound anchors for content hosted on Selected Work.
  const legacyHashes = new Set(['impact', 'work', 'waken', 'twinchat-paper', 'research', 'filmography']);
  if (!document.getElementById('selected-work') && legacyHashes.has(location.hash.slice(1))) {
    location.replace('selected-work.html' + location.hash);
  }

  // Each editorial row owns a motion identity; nested cards inherit its palette
  // and alternate their entrance direction rather than repeating one global fade.
  const sceneDefinitions = [
    ['#home', 'portrait-open', 'bloom', 'rise', '117,225,244', 900, 24],
    ['#proof', 'data-cascade', 'rise', 'rise', '117,225,244', 650, 12],
    ['#professional-profile', 'document-settle', 'curtain', 'settle', '151,195,226', 780, 10],
    ['.selected-work-gateway', 'path-crossing', 'sweep', 'slide', '117,225,244', 700, 16],
    ['#clineflow', 'memory-flow', 'scan', 'slide', '96,222,242', 860, 18],
    ['#memearcade', 'arcade-pop', 'prism', 'scale', '197,145,255', 740, 20],
    ['#wwdc14', 'apple-spotlight', 'spotlight', 'scale', '218,235,245', 980, 12],
    ['#citations', 'reference-stack', 'stack', 'settle', '166,173,234', 820, 14],
    ['#books', 'page-turn', 'page', 'slide', '215,207,189', 920, 16],
    ['.featured-book-section', 'reading-light', 'sweep', 'slide', '213,201,184', 880, 10],
    ['#interviews', 'screen-widen', 'curtain', 'scale', '137,201,220', 760, 12],
    ['#press', 'masthead', 'scan', 'slide', '205,224,235', 680, 10],
    ['#about', 'portrait-drift', 'bloom', 'slide', '171,164,219', 960, 22],
    ['#eb1a', 'recognition', 'spotlight', 'rise', '222,225,208', 1020, 14],
    ['.quote-section', 'quiet-resolve', 'page', 'settle', '205,221,229', 1100, 8],
    ['#selected-work', 'spatial-open', 'prism', 'scale', '117,225,244', 960, 24],
    ['.work-index', 'chapter-path', 'sweep', 'slide', '146,202,220', 620, 8],
    ['#impact', 'momentum', 'stack', 'rise', '112,216,238', 720, 18],
    ['#waken', 'awakening', 'bloom', 'scale', '162,155,238', 1020, 20],
    ['#work', 'product-unfold', 'page', 'slide', '131,194,232', 820, 18],
    ['#twinchat-paper', 'abstract-reveal', 'scan', 'settle', '173,164,231', 900, 10],
    ['#research', 'discovery-orbit', 'orbit', 'rise', '113,213,212', 1040, 22],
    ['#filmography', 'cinema-curtain', 'curtain', 'slide', '182,179,230', 1100, 16],
    ['#casual-books', 'reading-flow', 'sweep', 'rise', '215,207,189', 920, 12],
    ['.signal-footer', 'invitation', 'spotlight', 'scale', '117,225,244', 900, 12]
  ];
  const sceneRoots = new Map();
  const defaultScene = {name:'editorial', effect:'bloom', entrance:'rise', duration:650, travel:24};
  sceneDefinitions.forEach(([selector,name,effect,entrance,color,duration,travel]) => {
    document.querySelectorAll(selector).forEach(element => {
      element.dataset.sceneRoot = 'true'; element.dataset.scene = name;
      element.classList.add('scene-row');
      element.style.setProperty('--scene-color', color);
      element.style.setProperty('--scene-animation', `scene-${effect}`);
      element.style.setProperty('--scene-duration', `${duration}ms`);
      sceneRoots.set(element, {name,effect,entrance,duration,travel});
    });
  });

  // Every chapter has an entrance; nested blocks use a restrained stagger.
  // Nothing is hidden in CSS: unsupported APIs and script failures leave content readable.
  const selectors = [
    ['.signal-copy > *, .work-intro-inner > *', 'type'],
    ['.portrait-stage, .work-orbit', 'depth'],
    ['main > section', 'chapter'],
    ['.featured-book-section, .signal-footer', 'chapter'],
    ['.section-header, .selected-work-gateway-inner > h2', 'type'],
    ['.stat-item, .selected-work-link, .book-card, .press-card, .citation-card, .citation-house-card, .interview-card, .innovation-card', 'block'],
    ['.work-index, .waken-inner, .impact-card, .project-card, .clineflow-installer-shell, .clineflow-support, .meme-arcade-inner, .wwdc14-inner, .citations-intro, .professional-profile-inner, .featured-book-inner, .bio-content, .contact-callout, .footer-details', 'frame']
  ];
  const seen = new WeakSet();
  const targets = new Map();
  selectors.forEach(([selector, kind]) => {
    document.querySelectorAll(selector).forEach((element, index) => {
      const scene = sceneRoots.get(element.closest('[data-scene-root]')) || defaultScene;
      const direction = index % 2 ? -1 : 1;
      targets.set(element, { kind, scene, direction, delay: (index % 3) * 65 });
      element.dataset.transition = scene.name;
      element.dataset.entranceState = 'pending';
      element.style.setProperty('--scene-direction', String(direction));
      element.dataset.motion = kind;
      if (kind === 'frame' || kind === 'block') element.classList.add('motion-frame');
    });
  });
  function finishEntrance(element) {
    seen.add(element);
    const record = animations.get(element);
    if (record) record.animation.cancel();
    animations.delete(element);
    element.classList.remove('is-arriving');
    element.classList.remove('motion-offscreen');
    element.dataset.entranceState = 'complete';
    entranceObserver?.unobserve(element);
  }
  const entranceObserver = 'IntersectionObserver' in window && Element.prototype.animate ? new IntersectionObserver(entries => {
    for (const entry of entries) {
      const element = entry.target;
      const record = animations.get(element);
      if (record) {
        // Fast scrolling consumes the entrance; returning must show a settled row.
        if (!entry.isIntersecting) finishEntrance(element);
        continue;
      }
      if (!entry.isIntersecting || seen.has(element) || element.dataset.entranceState === 'complete') continue;
      seen.add(element);
      if (reduced || element.contains(document.activeElement)) { finishEntrance(element); continue; }
      const { kind, delay, scene, direction } = targets.get(element);
      const mobile = compactQuery.matches || !fineQuery.matches;
      const duration = mobile ? 360 : scene.duration;
      let frames;
      if (kind === 'chapter' || kind === 'frame') {
        // The clock controls decorative light only: nested fades would dim controls.
        frames = [{ opacity: 1 }, { opacity: 1 }];
      } else if (kind === 'depth' && !mobile) {
        frames = [
          { opacity: .55, transform: 'perspective(1000px) translateY(20px) rotateY(-4deg) scale(.97)', offset: 0 },
          { opacity: .95, transform: 'perspective(1000px) translateY(4px) rotateY(-.6deg) scale(.995)', offset: .65 },
          { opacity: 1, transform: 'perspective(1000px) translateY(0) rotateY(0) scale(1)', offset: 1 }
        ];
      } else {
        const entrances = {
          rise: 'translateY(24px)',
          settle: 'translateY(-14px)',
          slide: `translateX(${direction * 22}px)`,
          scale: 'translateY(8px) scale(.975)'
        };
        frames = [{ opacity: .55, transform: mobile ? 'translateY(8px)' : entrances[scene.entrance] }, { opacity: 1, transform: 'translate(0,0) scale(1)' }];
      }
      const entranceDelay = mobile ? 0 : delay;
      element.style.setProperty('--entrance-delay', `${entranceDelay}ms`);
      const animation = element.animate(frames, { duration, delay: entranceDelay, iterations: 1, easing: 'cubic-bezier(.16,1,.3,1)', fill: 'backwards' });
      animations.set(element, { animation, visible: true });
      element.dataset.entranceState = 'running';
      element.classList.add('is-arriving');
      animation.onfinish = () => finishEntrance(element);
    }
    syncPlayback();
  }, { threshold: .06 }) : null;
  if (entranceObserver) targets.forEach((_, element) => entranceObserver.observe(element));
  const settleEntrances = () => {
    for (const element of animations.keys()) finishEntrance(element);
  };
  compactQuery.addEventListener('change', settleEntrances);
  fineQuery.addEventListener('change', settleEntrances);
  window.addEventListener('pageshow', event => {
    if (event.persisted) { settleEntrances(); syncPlayback(); }
  });
  document.addEventListener('focusin', event => {
    for (const element of animations.keys()) if (element.contains(event.target)) finishEntrance(element);
  });

  // Scroll depth is decoration-only for cards and media. No perpetual frame loop.
  const depthEntries = new Map();
  const visibleDepth = new Set();
  const depthEnabled = () => !stopped() && !compactQuery.matches && fineQuery.matches;
  function measureDepth() {
    depthEntries.forEach((entry, element) => {
      const rect = element.getBoundingClientRect();
      entry.top = rect.top + window.scrollY; entry.height = rect.height;
    });
    scheduleDepth();
  }
  function renderDepth() {
    pointerFrame = 0;
    if (!depthEnabled()) return;
    // Sample only requested frames. Idle time never counts as a slow frame.
    frameSamples.push(performance.now() - frameQueuedAt);
    if (frameSamples.length === 20) {
      const slowFrames = frameSamples.filter(ms => ms > 50).length;
      frameSamples = [];
      if (slowFrames >= 12) {
        if (depthQuality === 1) {
          depthQuality = .5; root.dataset.motionQuality = 'calm'; resetDepth();
        } else {
          performanceReduced = true; root.dataset.motionQuality = 'static'; syncMotion(); return;
        }
      }
    }
    const scrollTop = window.scrollY, viewportHeight = window.innerHeight;
    visibleDepth.forEach(element => {
      const entry = depthEntries.get(element);
      const progress = Math.max(-1, Math.min(1, ((scrollTop + viewportHeight / 2) - (entry.top + entry.height / 2)) / ((viewportHeight + entry.height) / 2)));
      element.style.setProperty('--scroll-depth-y', `${(progress * entry.range * depthQuality).toFixed(2)}px`);
      element.style.setProperty('--scroll-depth-x', `${(progress * entry.horizontal * depthQuality).toFixed(2)}px`);
      element.style.setProperty('--scroll-depth-light', `${(38 + progress * 24).toFixed(1)}%`);
    });
    if (rig && stageVisible && depthQuality === 1) {
      rig.style.setProperty('--tilt-x', `${-pointer.y * 4}deg`);
      rig.style.setProperty('--tilt-y', `${pointer.x * 4}deg`);
    }
  }
  function scheduleDepth() {
    if (depthEnabled() && !pointerFrame && visibleDepth.size) {
      frameQueuedAt = performance.now(); pointerFrame = requestAnimationFrame(renderDepth);
    }
  }
  targets.forEach(({kind,scene,direction}, element) => {
    if (!['chapter','frame','block'].includes(kind)) return;
    const layer = document.createElement('span'); layer.className = 'scroll-depth-layer'; layer.setAttribute('aria-hidden', 'true');
    element.appendChild(layer); element.classList.add('has-scroll-depth');
    const rect = element.getBoundingClientRect();
    depthEntries.set(element, {top:rect.top+window.scrollY,height:rect.height,range:kind==='chapter'?scene.travel:Math.min(12,scene.travel),horizontal:direction*Math.min(8,scene.travel/3)});
  });
  const depthObserver = 'IntersectionObserver' in window ? new IntersectionObserver(entries => {
    entries.forEach(entry => {
      if (entry.isIntersecting) visibleDepth.add(entry.target); else visibleDepth.delete(entry.target);
    }); scheduleDepth();
  }, {rootMargin:'80px'}) : null;
  if (depthObserver) depthEntries.forEach((_,element)=>depthObserver.observe(element));
  function updateDepthPolicy() {
    if (depthEnabled()) scheduleDepth();
    else {
      frameSamples = [];
      resetDepth();
      depthEntries.forEach((_,element)=>{element.style.removeProperty('--scroll-depth-y');element.style.removeProperty('--scroll-depth-x');element.style.removeProperty('--scroll-depth-light');});
    }
  }
  playbackSubscribers.push(updateDepthPolicy);
  compactQuery.addEventListener('change', updateDepthPolicy);
  fineQuery.addEventListener('change', updateDepthPolicy);
  window.addEventListener('scroll', () => {
    pointer = {x:0,y:0}; stageRect = null; scheduleDepth();
  }, {passive:true});
  window.addEventListener('resize', measureDepth, {passive:true});
  if ('ResizeObserver' in window && document.querySelector('main')) new ResizeObserver(measureDepth).observe(document.querySelector('main'));

  // One demand-driven frame for pointer depth; no idle animation loop.
  function measureStage() { if (stage) stageRect = stage.getBoundingClientRect(); }
  if (stage && rig) {
    measureStage();
    if ('ResizeObserver' in window) new ResizeObserver(measureStage).observe(stage);
    if ('IntersectionObserver' in window) new IntersectionObserver(entries => {
      stageVisible = entries[0].isIntersecting;
      if (stageVisible) measureStage(); else resetDepth();
    }).observe(stage);
    else stageVisible = true;
    stage.addEventListener('pointerenter', measureStage, { passive: true });
    stage.addEventListener('pointermove', event => {
      if (stopped() || !stageVisible || compactQuery.matches || !fineQuery.matches || event.pointerType === 'touch') return;
      if (!stageRect) measureStage();
      const rect = stageRect;
      if (!rect?.width || !rect.height) return;
      pointer = { x: Math.max(-1, Math.min(1, (event.clientX - rect.left) / rect.width * 2 - 1)), y: Math.max(-1, Math.min(1, (event.clientY - rect.top) / rect.height * 2 - 1)) };
      scheduleDepth();
    }, { passive: true });
    stage.addEventListener('pointerleave', resetDepth, { passive: true });
    fineQuery.addEventListener('change', resetDepth);
  }

  // The press strip shares the same visibility and motion policy as entrances.
  const marquee = document.querySelector('.proof-marquee');
  if (marquee) {
    const pressButton = document.querySelector('.press-pause');
    let pressVisible = false, pressPaused = false, pressHovered = false;
    const updatePress = () => {
      const pause = stopped() || !pressVisible || pressPaused || pressHovered;
      marquee.classList.toggle('is-live', !reduced);
      marquee.classList.toggle('is-paused', pause);
      pressButton.textContent = pressPaused ? 'Play logos' : 'Pause logos';
      pressButton.disabled = reduced;
    };
    pressButton.hidden = false;
    pressButton.addEventListener('click', () => { pressPaused = !pressPaused; updatePress(); });
    marquee.addEventListener('pointerenter', () => { pressHovered = true; updatePress(); });
    marquee.addEventListener('pointerleave', () => { pressHovered = false; updatePress(); });
    playbackSubscribers.push(updatePress);
    if ('IntersectionObserver' in window) new IntersectionObserver(entries => {
      pressVisible = entries[0].isIntersecting; updatePress();
    }).observe(marquee);
    else pressVisible = true;
    updatePress();
  }

  // Autoplay is a single visible-only timer. Manual navigation stops it until Play.
  const carousel = document.querySelector('.meme-carousel');
  if (carousel) {
    const slides = [...carousel.querySelectorAll('.meme-arcade-screen-card')];
    const pauseButton = carousel.querySelector('.carousel-pause');
    const position = carousel.querySelector('.carousel-position');
    const status = carousel.querySelector('.carousel-status');
    const gallery = carousel.querySelector('.meme-arcade-gallery');
    let current = 0, timer = 0, visible = false, paused = false, hovered = false;
    let slideAnimation = null, requestedPause = null;
    carousel.classList.add('is-carousel-live');
    carousel.querySelector('.carousel-controls').hidden = false;
    slides.forEach((slide, index) => { slide.hidden = index !== 0; });
    function updateCarousel() {
      clearTimeout(timer); timer = 0;
      const active = !stopped() && visible && !paused && !hovered;
      carousel.dataset.autoplay = active ? 'playing' : 'paused';
      pauseButton.textContent = paused ? 'Play' : 'Pause';
      pauseButton.setAttribute('aria-label', paused ? 'Play slideshow' : 'Pause slideshow');
      pauseButton.disabled = reduced;
      if (reduced) { pauseButton.textContent = 'Motion off'; pauseButton.setAttribute('aria-label', 'Slideshow disabled by reduced motion'); }
      if (!active) { slideAnimation?.cancel(); slideAnimation = null; }
      if (active) timer = setTimeout(() => { showSlide(current + 1, false); }, 3000);
    }
    function showSlide(index, manual) {
      slideAnimation?.cancel();
      current = (index + slides.length) % slides.length;
      slides.forEach((slide, i) => { slide.hidden = i !== current; });
      position.textContent = `${current + 1} / ${slides.length}`;
      carousel.querySelectorAll('.carousel-dot').forEach((dot, index) => dot.setAttribute('aria-current', String(index === current)));
      if (manual) { paused = true; status.textContent = `${current + 1} of ${slides.length}: ${slides[current].querySelector('figcaption').textContent}`; }
      updateCarousel();
      if (!stopped() && !manual && Element.prototype.animate) {
        slideAnimation = slides[current].animate([{opacity:.2},{opacity:1}], { duration: compactQuery.matches ? 250 : 450, easing:'ease-out' });
      }
    }
    carousel.querySelector('.carousel-prev').addEventListener('click', () => showSlide(current - 1, true));
    carousel.querySelector('.carousel-next').addEventListener('click', () => showSlide(current + 1, true));
    carousel.querySelectorAll('.carousel-dot').forEach(dot => dot.addEventListener('click', () => showSlide(Number(dot.dataset.slide), true)));
    pauseButton.addEventListener('pointerdown', () => { requestedPause = !paused; });
    pauseButton.addEventListener('click', () => {
      paused = requestedPause === null ? !paused : requestedPause;
      requestedPause = null;
      status.textContent = paused ? 'Slideshow paused' : 'Slideshow playing'; updateCarousel();
    });
    carousel.addEventListener('focusin', () => { paused = true; updateCarousel(); });
    carousel.addEventListener('pointerdown', () => { paused = true; updateCarousel(); }, {passive:true});
    carousel.addEventListener('pointerenter', event => { if (event.pointerType !== 'touch') { hovered = true; updateCarousel(); } });
    carousel.addEventListener('pointerleave', () => { hovered = false; updateCarousel(); });
    carousel.addEventListener('keydown', event => {
      if (event.key === 'ArrowRight' || event.key === 'ArrowLeft') { event.preventDefault(); showSlide(current + (event.key === 'ArrowRight' ? 1 : -1), true); }
    });
    let touchStart = null;
    gallery.style.touchAction = 'pan-y';
    gallery.addEventListener('pointerdown', event => { if (event.pointerType === 'touch') touchStart = {x:event.clientX,y:event.clientY}; }, {passive:true});
    gallery.addEventListener('pointerup', event => {
      if (!touchStart) return;
      const dx = event.clientX-touchStart.x, dy = event.clientY-touchStart.y; touchStart = null;
      if (Math.abs(dx)>45 && Math.abs(dx)>Math.abs(dy)*1.5) showSlide(current+(dx<0?1:-1),true);
    }, {passive:true});
    gallery.addEventListener('pointercancel', () => { touchStart = null; }, {passive:true});
    playbackSubscribers.push(updateCarousel);
    if ('IntersectionObserver' in window) new IntersectionObserver(entries => { visible = entries[0].isIntersecting; updateCarousel(); }, {threshold:.25}).observe(carousel);
    else visible = true;
    updateCarousel();
  }

  document.querySelectorAll('[data-copy-prompt]').forEach(button => {
    button.addEventListener('click', async () => {
      const prompt = document.getElementById(button.dataset.copyPrompt)?.textContent?.trim();
      const status = button.parentElement.querySelector('.copy-status');
      try {
        if (!prompt || !navigator.clipboard) throw new Error('Clipboard unavailable');
        await navigator.clipboard.writeText(prompt);
        status.textContent = 'Prompt copied';
      } catch (_) {
        status.textContent = 'Select and copy the prompt above.';
      }
    });
  });

  if ('IntersectionObserver' in window) {
    const navLinks = [...document.querySelectorAll('.desktop-links a[href^="#"]')];
    const navObserver = new IntersectionObserver(entries => {
      entries.forEach(entry => {
        if (!entry.isIntersecting) return;
        navLinks.forEach(link => {
          if (link.hash === '#' + entry.target.id) link.setAttribute('aria-current', 'location');
          else link.removeAttribute('aria-current');
        });
      });
    }, { rootMargin: '-15% 0px -65% 0px' });
    document.querySelectorAll('main > section[id]').forEach(section => navObserver.observe(section));
  }
})();
'''
