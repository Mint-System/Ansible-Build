module.exports = {
    title: 'Ansible Playbooks',
    description: 'Collection of Ansible playbooks and roles.',
    head: [
        ['link', { rel: "icon", type: "image/png", href: "icon.png"}],
    ],
    themeConfig: {
        logo: '/icon.png',
        sidebar: 'auto',
        repo: 'mint-system/ansible-playbooks',
        docsBranch: 'master',
        editLinks: true,
        nav: [
            { text: 'Home', link: '/' },
            { text: 'Mint System', link: 'https://www.mint-system.ch' }
        ],
    },
    dest: 'public',
}
