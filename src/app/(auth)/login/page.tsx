'use client';

import { useState } from 'react';

export default function Login() {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();

    // Simulação simples de validação
    if (!email || !password) {
      setError('Preencha todos os campos.');
      return;
    }

    setError('');

    // Aqui você pode chamar a API para autenticação
    console.log('Login com:', { email, password });
    
    // Exemplo: redirecionar após login bem-sucedido (você pode usar router.push)
  };

    return(
    <main className="max-w-md h-full mx-auto mt-20 p-6 border rounded shadow">
      <h1 className="text-2xl mb-6">Login</h1>
      
      <form onSubmit={handleSubmit} className="flex flex-col gap-4">
        <input
          type="email"
          placeholder="Email"
          className="p-2 border rounded"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          required
          autoFocus
        />

        <input
          type="password"
          placeholder="Senha"
          className="p-2 border rounded"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          required
        />

        {error && <p className="text-red-600">{error}</p>}

        <button
          type="submit"
          className="bg-blue-600 text-white py-2 rounded hover:bg-blue-700 transition"
        >
          Entrar
        </button>
      </form>
    </main>
    );
}