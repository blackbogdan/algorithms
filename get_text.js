ff=$('.promptContainer.editor-box .CodeMirror-scroll ')
ff.html().replace(/\b<.*?>\b/g, "\n").replace(/<.*?>/g, "").replace(/\&gt;/g, ">")
