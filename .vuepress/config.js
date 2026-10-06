import { viteBundler } from '@vuepress/bundler-vite'
import { defaultTheme } from '@vuepress/theme-default'
import { slimsearchPlugin } from '@vuepress/plugin-slimsearch'
import { shikiPlugin } from '@vuepress/plugin-shiki'
import { mermaidPlugin } from './mermaid'
import { plausiblePlugin } from './plausible'
import { defineUserConfig } from 'vuepress'
import { searchPlugin } from '@vuepress/plugin-search'
import path from 'node:path'
import { fileURLToPath } from 'node:url'

const __dirname = path.dirname(fileURLToPath(import.meta.url))

export default defineUserConfig({
    bundler: viteBundler({
        viteOptions: {
            build: {
                sourcemap: false,
                reportCompressedSize: false,
            },
        },
    }),
    lang: 'en-US',
    title: 'Ansible Build',
    description: 'Collection of Ansible playbooks and roles.',
    head: [
        ['link', { rel: 'icon', href: '/icon.png' }]
    ],
    pagePatterns: [
        'roles/**/*.md',
        'README.md',
        'roles.md',
        'scripts.md',
        'upgrade-odoo.md',
    ],
    dest: path.resolve(__dirname, 'dist'),
    public: path.resolve(__dirname, 'public'),
    temp: path.resolve(__dirname, '.temp'),
    cache: path.resolve(__dirname, '.cache'),
    theme: defaultTheme({
        logo: '/icon.png',
        repo: 'mint-system/ansible-build',
        docsBranch: 'main',
        editLink: true,
        navbar: [
            { text: 'Roles', link: '/roles' },
            { text: 'Scripts', link: '/scripts' },
            {
                text: 'Upgrade Odoo',
                link: '/upgrade-odoo',
            },
            { text: 'Chat', link: 'https://matrix.to/#/#ansible-build:mint-system.ch' }
        ],
    }),
    plugins: [
        slimsearchPlugin({
            indexContent: true,
            suggestion: false
        }),
        // searchPlugin({
        //   maxSuggestions: 10,
        // }),
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
