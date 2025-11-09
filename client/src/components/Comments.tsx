import { useEffect, useRef } from "react";

interface CommentsProps {
  title?: string;
  description?: string;
}

export default function Comments({ title = "Comentarios", description = "" }: CommentsProps) {
  const containerRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    if (!containerRef.current) return;

    // Limpiar comentarios previos si existen
    const existingScript = containerRef.current.querySelector("script");
    if (existingScript) {
      existingScript.remove();
    }

    // Crear el script de Utterances
    const script = document.createElement("script");
    script.src = "https://utteranc.es/client.js";
    script.async = true;
    script.crossOrigin = "anonymous";
    
    // Configuración de Utterances
    script.setAttribute("repo", "CaldeIsa/catalogo-pinturas-comentarios");
    script.setAttribute("issue-term", "pathname");
    script.setAttribute("label", "comments");
    script.setAttribute("theme", "light");
    script.setAttribute("loading", "lazy");

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
        className="utterances-container"
      />
    </div>
  );
}
