// import React, { useEffect, useState } from "react";
// import type { Product } from '@/app/types/types';


// export default function Reviews() {

//     const [product, setProduct] = useState<Product[]>([]);

//         useEffect(() => {
//             const fetchData = async () => {
//                 const data = await GetAllReviews();
//                 setProduct(data);
//             };
//             fetchData();
//         }, []);

//         if (!product) {
//             return (
//                 <div className="flex flex-col items-center justify-center text-2xl p-4">
//                     Carregando Produtos...
//                 </div>
//             );
//         }


//     return(
//         <section className="flex flex-col w-full justify-center items-center p-8 gap-2">
//             <h2 className="text-3xl p-4">O que nossos clientes dizem</h2>
//             <div className="flex gap-2 w-full justify-center items-center">
//                 <p>Lista de avaliações de clientes...</p>
//             </div>
//         </section>
//     );
// }