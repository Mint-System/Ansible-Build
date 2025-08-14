import { viteBundler } from '@vuepress/bundler-vite'
import { defaultTheme } from '@vuepress/theme-default'
import { slimsearchPlugin } from '@vuepress/plugin-slimsearch'
import { shikiPlugin } from '@vuepress/plugin-shiki'
import { mermaidPlugin } from './mermaid'
import { plausiblePlugin } from './plausible'
import { defineUserConfig } from 'vuepress'


export default defineUserConfig({
    bundler: viteBundler(),
    lang: 'en-US',
    title: 'Ansible Build',
    description: 'Collection of Ansible playbooks and roles.',
    head: [
        ['link', { rel: 'icon', href: '/icon.png' }]
    ],
    pagePatterns: ['**/*.md', '!.vuepress', '!node_modules', '!tmp', '!venvmain'],
    theme: defaultTheme({
        logo: '/icon.png',
        repo: 'mint-system/ansible-build',
        docsBranch: 'main',
        editLink: true,
        navbar: [
            { text: 'Home', link: '/' },
            { text: 'Roles', link: '/roles' },
            { text: 'Scripts', link: '/scripts' },
            { text: 'Mint System', link: 'https://www.mint-system.ch' },
            { text: 'Chat', link: 'https://matrix.to/#/!BgzMVlwDExHDQPPdKJ:mint-system.ch?via=mint-system.ch' }
        ],
    }),
    plugins: [
        slimsearchPlugin({
            indexContent: true,
            suggestion: false
        }),
        plausiblePlugin({
            'domain': 'ansible.build'
        }),
        mermaidPlugin(),
        shikiPlugin({
            theme: 'catppuccin-latte',
            langs: ['bash', 'yml', 'yaml', 'json', 'css', 'html', 'xml', 'groovy', 'py', 'python', 'sql', 'powershell', 'txt', 'csv', 'mermaid', 'md', 'markdown', 'toml', 'php'],
        })
    ],
})
