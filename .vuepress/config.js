import { defaultTheme } from 'vuepress'
import { searchPlugin } from '@vuepress/plugin-search'
import { plausiblePlugin } from './plausible'
import { defineUserConfig } from 'vuepress'


export default defineUserConfig({
    lang: 'en-US',
    title: 'Ansible Build',
    description: 'Collection of Ansible playbooks and roles.',
    head: [
        ['link', { rel: 'icon', href: '/icon.png' }]
    ],
    theme: defaultTheme({
        logo: '/icon.png',
        repo: 'mint-system/ansible-playbooks',
        docsBranch: 'master',
        editLink: true,
        navbar: [
            { text: 'Home', link: '/' },
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