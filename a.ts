import Bun from "bun";

const path = "dashboard.html";
const file = Bun.file(path);
const resp = new Response(file);
Bun.serve({
  routes:{
    "/": new Response(file),
  }
});