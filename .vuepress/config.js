import { viteBundler } from '@vuepress/bundler-vite'
import { defaultTheme } from '@vuepress/theme-default'
import { searchPlugin } from '@vuepress/plugin-search'
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
    pagePatterns: ['**/*.md', '!.vuepress', '!node_modules', '!tmp', '!venvmaster'],
    theme: defaultTheme({
        logo: '/icon.png',
        repo: 'mint-system/ansible-build',
        docsBranch: 'master',
        editLink: true,
        navbar: [
            { text: 'Home', link: '/' },
            { text: 'Scripts', link: '/scripts' },
            { text: 'Mint System', link: 'https://www.mint-system.ch' }
        ],
    }),
    plugins: [
        searchPlugin({
            maxSuggestions: 10
        }),
        plausiblePlugin({
            'domain': 'ansible.build'
        }),
    ],
})