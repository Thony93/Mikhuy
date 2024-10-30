// src/pages/Home.jsx

import React, { useState, useEffect } from "react";
import { Link } from "react-router-dom";
import Header from "../components/Header";
import Footer from "../components/Footer";
import "../styles/Home.css";
import axios from "axios";

function Home() {
  const [audiolibros, setLibros] = useState([]);
  const [loading, setLoading] = useState(true);
  const [query, setQuery] = useState("");

  const handleSearch = async () => {
    if (query.trim() !== "") {
      setLoading(true);
      try {
        const response = await axios.get(`http://localhost:8000/api/libros/buscar/?search=${query}`);
        setLibros(response.data); // Almacena los resultados de búsqueda
      } catch (error) {
        console.error("Error al buscar libros:", error);
      } finally {
        setLoading(false);
      }
    }
  };

  useEffect(() => {
    const fetchLibros = async () => {
      try {
        const response = await axios.get("http://localhost:8000/api/libros/");
        setLibros(response.data);
        setLoading(false);
      } catch (error) {
        console.error("Error fetching the audiobooks", error);
        setLoading(false);
      }
    };

    fetchLibros();
  }, []);

  if (loading) {
    return (
      <div className="spinner center">
        <div className="spinner-blade"></div>
        <div className="spinner-blade"></div>
        <div className="spinner-blade"></div>
        <div className="spinner-blade"></div>
        <div className="spinner-blade"></div>
        <div className="spinner-blade"></div>
        <div className="spinner-blade"></div>
        <div className="spinner-blade"></div>
        <div className="spinner-blade"></div>
        <div className="spinner-blade"></div>
        <div className="spinner-blade"></div>
        <div className="spinner-blade"></div>
      </div>
    );
  }

  return (
    <div className="home-page">
      <Header query={query} setQuery={setQuery} onSearch={handleSearch}/>
      <main className="home-main-content">
        {/* Sección superior con imagen y frase */}
        <section className="hero-section">
          <img
            src="/assets/FondoMikhuy.png"
            alt="Imagen Hero"
            className="hero-image"
          />
          <div className="hero-content">
            <p className="hero-description">
              Disfruta de un formato cómodo y moderno que te permite aprender
              sobre la gastronomía sin dejar de hacer lo que amas: ¡cocinar!
            </p>
            <h4 className='nombre-equipo'></h4>
          </div>
        </section>
        
        {/* Contenedor común para el título y las tarjetas */}
        <div className="section-content">
          {/* Título "Empieza a escuchar" */}
          <h2 className="section-title">EMPIEZA A ESCUCHAR</h2>

          {/* Grid de audiolibros */}
          <section className="audiobooks-grid">
            {audiolibros.map((audiolibro) => (
              <Link
                to={`/audiolibro/${audiolibro.id_libro}`}
                className="audiobook-card"
                key={audiolibro.id_libro}
              >
                <div className="image-container">
                  <img
                    className="capa1"
                    src={audiolibro.url_imagen_portada}
                    alt={audiolibro.nombre_libro}
                  />
                  <p className="capa2">Pruebita</p>
                </div>
                <div className="audiobook-title">
                  {audiolibro.nombre_libro}
                </div>
                <div className="audiobook-year">
                  {audiolibro.fecha_publicacion}
                </div>
              </Link>
            ))}
          </section>
        </div>
      </main>
      <Footer />
    </div>
  );
}

export default Home;
