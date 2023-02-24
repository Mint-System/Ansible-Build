import { defineClientConfig } from '@vuepress/client'

const { domain = undefined } = __PLAUSIBLE_OPTIONS__

export default defineClientConfig({
	enhance({ router }) {
		if (!__VUEPRESS_SSR__) {
			var script = document.createElement('script')
			script.defer = true
			script.dataset.domain = domain
			script.src = "https://plausible.io/js/script.js"
			document.getElementsByTagName('head')[0].appendChild(script)
		}	
	}
})
