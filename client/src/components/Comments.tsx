import { useEffect, useRef } from "react";

interface CommentsProps {
  title?: string;
  description?: string;
}

export default function Comments({ title = "Comentarios", description = "" }: CommentsProps) {
  const containerRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    if (!containerRef.current) return;

    // Crear el script de Utterances con atributos adicionales
    const script = document.createElement("script");
    script.src = "https://utteranc.es/client.js";
    script.async = true;
    script.crossOrigin = "anonymous";
    
    // Configuración de Utterances
    script.setAttribute("repo", "CaldeIsa/catalogo-pinturas-comentarios");
    script.setAttribute("issue-term", "pathname");
    script.setAttribute("theme", "light");
    script.setAttribute("label", "comments");
    script.setAttribute("loading", "lazy");

    // Limpiar contenido previo
    containerRef.current.innerHTML = "";
    
    // Agregar el script
    containerRef.current.appendChild(script);
  }, []);

  return (
    <div className="mt-12 pt-8 border-t border-border">
      <h2 className="text-2xl font-bold mb-2 text-foreground">{title}</h2>
      {description && (
        <p className="text-muted-foreground mb-6">{description}</p>
      )}
      <div 
        ref={containerRef}
        className="w-full"
        style={{ minHeight: "400px" }}
      />
    </div>
  );
}
