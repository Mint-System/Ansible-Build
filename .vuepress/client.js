import { defineClientConfig } from 'vuepress/client'
import { defineSearchConfig } from '@vuepress/plugin-slimsearch/client'
import Layout from './layouts/Layout.vue'

// A snippet is an array of tokens: plain strings, or ['mark', matchedText] tuples.
const flattenSnippet = (snippet) =>
  snippet.map((word) => (Array.isArray(word) ? word[1] : word)).join('')

defineSearchConfig({
  combineWith: 'AND',
  resultsFilter: (results, query) => {
    const phrase = query.trim().toLowerCase()
    if (!phrase.includes(' ')) return results // single word — no phrase check needed

    return results
      .map((result) => {
        const matchedContents = result.contents
          .map((item) => {
            const matchedSnippets = item.display.filter((snippet) =>
              flattenSnippet(snippet).toLowerCase().includes(phrase),
            )
            return matchedSnippets.length
              ? { ...item, display: matchedSnippets }
              : null
          })
          .filter(Boolean)

        return matchedContents.length
          ? { ...result, contents: matchedContents }
          : null
      })
      .filter(Boolean)
  },
})

export default defineClientConfig({
  layouts: {
    Layout,
  },
})