export default function Faq() {
    return (
        <section className="max-w-4xl mx-auto mt-10 p-6">
            <h1 className="text-3xl font-bold mb-6">Perguntas Frequentes (FAQ)</h1>
            <div className="mb-4">
                <h2 className="text-xl font-semibold">1. Quais são os métodos de pagamento aceitos?</h2>
                <p>Aceitamos cartões de crédito, débito, PayPal e transferência bancária.</p>
            </div>
            <div className="mb-4">
                <h2 className="text-xl font-semibold">2. Qual é o prazo de entrega?</h2>
                <p>O prazo de entrega varia conforme a localização, mas geralmente é entre 5 a 10 dias úteis.</p>
            </div>
            <div className="mb-4">
                <h2 className="text-xl font-semibold">3. Posso devolver um produto?</h2>
                <p>Sim, aceitamos devoluções em até 30 dias após a compra, desde que o produto esteja em sua embalagem original e sem uso.</p>
            </div>
            {/* Adicione mais perguntas frequentes aqui */}
        </section>
    );
}