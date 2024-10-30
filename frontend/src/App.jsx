// src/App.jsx

import React from "react";
import { Routes, Route } from "react-router-dom";
import Home from "./pages/Home";
import Audiolibro from "./pages/Audiolibro";
import "./styles/App.css";
import Recetas from "./pages/Recetas";
import Receta from "./pages/Receta"; 

function App() {
  return (
    <div className="app-container">
      <div className="page-container">
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/audiolibro/:id_libro" element={<Audiolibro />} />
          <Route path="/recetas" element={<Recetas />} />
          <Route path="/receta/:id_receta" element={<Receta />} />
          {/* Otras rutas si las hay */}
        </Routes>
      </div>
    </div>
  );
}

export default App;