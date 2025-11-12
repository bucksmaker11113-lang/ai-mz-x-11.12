import React, { useRef } from "react";
import { Canvas, useFrame } from "@react-three/fiber";
import { OrbitControls, Sphere, PointLightHelper } from "@react-three/drei";

function FusionCore() {
  const sphereRef = useRef();
  useFrame(({ clock }) => {
    const t = clock.getElapsedTime();
    sphereRef.current.scale.setScalar(1 + Math.sin(t * 2) * 0.05);
    sphereRef.current.rotation.y += 0.005;
  });

  return (
    <Sphere ref={sphereRef} args={[1.4, 64, 64]}>
      <meshStandardMaterial
        emissive="#00f6ff"
        emissiveIntensity={2.5}
        roughness={0.3}
        metalness={0.8}
      />
    </Sphere>
  );
}

export default function FusionCanvas() {
  return (
    <Canvas camera={{ position: [0, 0, 5] }}>
      <ambientLight intensity={0.3} />
      <pointLight position={[5, 5, 5]} intensity={1.5} color="#00f6ff" />
      <FusionCore />
      <OrbitControls enableZoom={false} />
    </Canvas>
  );
}
