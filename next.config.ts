import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  images: {
    domains: ["cdn.dummyjson.com"], // 👈 libera o domínio do seu CDN
  },  
};

export default nextConfig;
