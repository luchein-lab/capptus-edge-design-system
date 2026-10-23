/* Local, progressively enhanced image selector. No external services. */
(() => {
  const picker = document.getElementById('image-select');
  const image = document.getElementById('collage');
  const status = document.getElementById('image-status');
  if (!picker || !image || !status) return;
  const names = new Map(Array.from(picker.options, option => [option.value, option.text]));
  picker.addEventListener('change', () => {
    if (!names.has(picker.value)) return;
    const name = names.get(picker.value);
    status.textContent = `Loading ${name}…`;
    image.onload = () => { status.textContent = `${name} · generated concept imagery`; };
    image.onerror = () => { status.textContent = 'Image unavailable. Keep the assets folder beside this reference.'; };
    image.alt = `${name}: generated Baja photographic collage`;
    image.src = `assets/imagery/baja/images/${picker.value}.png`;
  });
})();
