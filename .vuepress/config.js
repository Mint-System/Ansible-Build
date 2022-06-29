const { defaultTheme } = require('vuepress')
const { searchPlugin } = require('@vuepress/plugin-search')

module.exports = {
    lang: 'en-US',
    title: 'Ansible Playbooks',
    description: 'Collection of Ansible playbooks and roles.',
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
        searchPlugin(),
    ],
}