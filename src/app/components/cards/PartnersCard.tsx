import Image, { StaticImageData } from "next/image";

type PartnerCardsProps = {
  image: StaticImageData;
};

export default function PartnerCards({ image }: PartnerCardsProps) {
  return (
        <section className="w-full h-20 flex items-center justify-center">
            <Image 
            src={image}
            alt="Parceiros da IluminaCasa"
            width={100}
            height={100}
            className="object-contain sm:h-[3.125rem] sm:w-50 w-[50px] h-[50px]"
            />
        </section>
    );
}
