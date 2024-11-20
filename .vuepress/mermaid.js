import { path } from '@vuepress/utils'

const name = '@mint-system/plugin-mermaid'

const mermaidPlugin = () => {
    return {
        name,
        clientConfigFile: path.resolve(__dirname, 'mermaidClient.js'),
        extendsMarkdown: md => {
            const defaultFence = md.renderer.rules.fence

            md.renderer.rules.fence = (tokens, idx, options, env, self) => {
                const token = tokens[idx]
                const code = token.content.trim()

                if (token.info === 'mermaid') {
                    return `<pre style="background-color:#fff;" class="mermaid">${md.utils.escapeHtml(code)}</pre>`
                }

                return defaultFence(tokens, idx, options, env, self)
            }
        }
    }
}

export { mermaidPlugin }