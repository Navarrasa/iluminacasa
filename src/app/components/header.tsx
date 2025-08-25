"use client";
import { useMediaQuery } from "@mui/material";
import { MobileAccountMenu } from "@/app/components/ui/mobileaccountmenu";
import { DesktopAccountMenu } from "@/app/components/ui/desktopaccountmenu";
import { Navbar } from "@/app/components/ui/navbar";
export function Header() {
  
  const isMobile = useMediaQuery("(max-width: 689px)");

  return (
    <header className="flex justify-between p-4 w-full h-auto fixed">
      <div className="w-full flex items-center justify-between sm:p-8 p-2">
        {/* Logo */}
        <div className="sm:text-3xl text-2xl font-federant tracking-wider">IluminaCasa</div>

        {isMobile && <MobileAccountMenu />}

        {/* Navegação - agora separada */}
        {!isMobile && <Navbar />}
        {/* Menu para Desktop/Tablets */}
        {!isMobile && <DesktopAccountMenu />}
      </div>
    </header>
  );
}
