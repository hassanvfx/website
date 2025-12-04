import * as React from "react";
import { Box } from "@mui/material";
import { keyframes } from "@mui/system";
import { ALL_CDN_IMAGES } from "../config/cdnImageMap";

export interface FadingGalleryProps {
  images?: string[];
  displayMs?: number;
  transitionMs?: number;
  fadeColor?: string;
  overlayGradient?: string;
  scaling?: number;
}

export const FadingGallery: React.FC<FadingGalleryProps> = ({
  images = ALL_CDN_IMAGES,
  displayMs = 4000,
  transitionMs = 1200,
  fadeColor = "#000",
  overlayGradient = "radial-gradient(ellipse at center, rgba(0,0,0,0.3) 0%, rgba(0,0,0,0.85) 70%, rgba(0,0,0,0.95) 100%)",
  scaling = 1.12,
}) => {
  const [active, setActive] = React.useState<number>(0);
  const [phase, setPhase] = React.useState<"idle" | "fade_in" | "fade_out">("idle");
  const [loadedImages, setLoadedImages] = React.useState<string[]>([]);
  const [isLoading, setIsLoading] = React.useState(true);

  const half = Math.max(60, Math.floor(transitionMs / 2));

  // Shuffle and preload images
  React.useEffect(() => {
    const shuffled = [...images].sort(() => Math.random() - 0.5);
    const preloadCount = Math.min(10, shuffled.length);
    
    let loadedCount = 0;
    const loaded: string[] = [];
    
    shuffled.slice(0, preloadCount).forEach((src) => {
      const img = new Image();
      img.onload = () => {
        loaded.push(src);
        loadedCount++;
        if (loadedCount >= 3) {
          setLoadedImages([...loaded]);
          setIsLoading(false);
        }
      };
      img.onerror = () => {
        loadedCount++;
      };
      img.src = src;
    });

    // Add remaining images after initial load
    setTimeout(() => {
      setLoadedImages(shuffled.filter(src => !loaded.includes(src)).concat(loaded));
    }, 5000);
  }, [images]);

  // Animation loop
  React.useEffect(() => {
    if (loadedImages.length <= 1 || isLoading) return;
    
    let mounted = true;
    let t1: ReturnType<typeof setTimeout>;
    let t2: ReturnType<typeof setTimeout>;
    let t3: ReturnType<typeof setTimeout>;

    const run = () => {
      t1 = setTimeout(() => {
        if (!mounted) return;
        setPhase("fade_in");

        t2 = setTimeout(() => {
          if (!mounted) return;
          setActive((prev) => (prev + 1) % loadedImages.length);
          setPhase("fade_out");

          t3 = setTimeout(() => {
            if (!mounted) return;
            setPhase("idle");
            run();
          }, half);
        }, half);
      }, displayMs);
    };

    run();
    return () => {
      mounted = false;
      clearTimeout(t1);
      clearTimeout(t2);
      clearTimeout(t3);
    };
  }, [loadedImages.length, displayMs, half, isLoading]);

  const zoomKeyframes = React.useMemo(
    () => keyframes`
      from { transform: translateZ(0) scale(1); }
      to   { transform: translateZ(0) scale(${scaling}); }
    `,
    [scaling]
  );

  const zoomDuration = displayMs + half + 120;

  if (isLoading || loadedImages.length === 0) {
    return (
      <Box
        sx={{
          position: "fixed",
          inset: 0,
          zIndex: -1,
          backgroundColor: fadeColor,
        }}
        aria-hidden
      />
    );
  }

  return (
    <Box
      sx={{
        position: "fixed",
        inset: 0,
        zIndex: -1,
        overflow: "hidden",
        pointerEvents: "none",
      }}
      aria-hidden
    >
      {/* Current image */}
      {loadedImages[active] && (
        <Box
          key={active}
          sx={{
            position: "absolute",
            inset: 0,
            backgroundImage: `url("${loadedImages[active]}")`,
            backgroundSize: "cover",
            backgroundPosition: "center",
            backgroundRepeat: "no-repeat",
            transformOrigin: "center center",
            willChange: "transform",
            animation: `${zoomKeyframes} ${zoomDuration}ms linear 0ms 1 forwards`,
          }}
        />
      )}

      {/* Gradient overlay */}
      {overlayGradient && (
        <Box
          sx={{
            position: "absolute",
            inset: 0,
            background: overlayGradient,
          }}
        />
      )}

      {/* Fade layer */}
      <Box
        sx={{
          position: "absolute",
          inset: 0,
          backgroundColor: fadeColor,
          opacity: phase === "fade_in" ? 1 : 0,
          transition: `opacity ${half}ms ease-in-out`,
          willChange: "opacity",
        }}
      />
    </Box>
  );
};

export default FadingGallery;
