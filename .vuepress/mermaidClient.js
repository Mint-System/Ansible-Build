import { defineClientConfig } from '@vuepress/client'
import mermaid from 'mermaid'

export default defineClientConfig({
    enhance({ router }) {
        if (!__VUEPRESS_SSR__) {
            mermaid.initialize({ startOnLoad: true })
            router.afterEach(() => {
                mermaid.contentLoaded()
            })
        }
    }
})
