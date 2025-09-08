import Image from "next/image";
import { storeImages } from "@/data/images";

export default function HeroAboutTheStore() {
  return (
    <section className="w-full h-auto relative">
        <section>
            <Image
              src={storeImages[0].image}
              alt="Imagem da loja"
              width={1440}
              height={400}
              priority
              style={{ width: "100%", height: "auto", objectFit: "cover" }}
            />
        </section>
    </section>
  );
}
