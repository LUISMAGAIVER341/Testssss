import { serve } from "bun";
import { writeFile, readFile } from "fs/promises";

serve({
  port: 3000,
  async fetch(req) {
    if (req.method === "PUT" && new URL(req.url).pathname === "/") {
      const json = await req.json();
      await writeFile("app/data.json", JSON.stringify(json, null, 2));
      return new Response("Arquivo salvo com sucesso", { status: 200 });
    }

    if (req.method === "GET" && new URL(req.url).pathname === "/") {
      const json = await readFile("app/data.json", "utf-8");
      return new Response(json, {
        headers: { "Content-Type": "application/json" },
      });
    }

    return new Response("Rota inválida", { status: 404 });
  },
});
