const BASE_URL = 'http://127.0.0.1:8000/api/v1/';


export const GetBestSellers = () => {
    fetch(`${BASE_URL}products/best-sellers`
        // TODO fazer um get no endpoint e retornar os dados da API
    )
}