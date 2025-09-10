const BASE_URL = 'http://127.0.0.1:8000/api/v1/';
import axios from "axios";

export const GetBestSellers = async () => {
    try {
        const response = await axios.get(`${BASE_URL}products/best-sellers`);
        return response.data;
    } catch (error) {
        console.error("Error fetching best sellers:", error);
        throw error;
    }
};
