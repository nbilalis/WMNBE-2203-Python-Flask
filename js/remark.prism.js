function parseLanguage(lang) {
  return (
    {
      js: "jsx",
    }[lang] || lang
  );
}

remark.highlighter.engine.highlightBlock = (block) => {
  const language = parseLanguage(block.className.split(" ")[0]);
  const prismLang = Prism.languages[language];

  console.log({language,prismLang});

  if (prismLang) {
    block.parentNode.className = `${block.parentNode.className} language-${language}`;
    const html = Prism.highlight(block.textContent, prismLang);

    const lines = html.split(`\n`);
    let currentSpan = null;

    for (var i = 0; i < lines.length; i++) {
      let line = lines[i];

      if (currentSpan) {
        line = currentSpan + line;
        currentSpan = null;
      }

      const openTags = [];
      const re = /(<span[^>]*>|<\/span>)/gi;
      let matches;

      while ((matches = re.exec(line)) != null) {
        const tag = matches[1];
        if (tag[1] === "/") {
          openTags.pop();
        } else {
          openTags.push(tag);
        }
      }

      currentSpan = openTags.join("");
      line = line + ("</" + "span>").repeat(openTags.length);
      lines[i] = line;
    }

    block.innerHTML = lines.join("\n");
  } else {
    console.warn(`Language '${language}' not supported?`);
  }
};
