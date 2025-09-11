export type Product = {
  title: string;
  category: string;
  price: number;
  discount: number;
  rating: number;
  reviews: string[];
  description: string;
  image: string[];
  tags?: string[];
};