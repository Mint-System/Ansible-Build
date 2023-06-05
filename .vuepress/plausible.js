import { path } from '@vuepress/utils'

const name = '@mint-system/plugin-plausible'

const plausiblePlugin = ({ domain }) => {
    return {
        name,
        clientConfigFile: path.resolve(__dirname, 'client.js'),
        define: {
            __PLAUSIBLE_OPTIONS__: { domain },
        },
    }
}

export { plausiblePlugin }