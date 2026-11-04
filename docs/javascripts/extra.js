// Plausible analytics
// Replicates the previous Vuepress plugin (@mint-system/plugin-plausible),
// which injected the Plausible script with data-domain = ansible.build.
;(function () {
  if (document.querySelector('script[data-domain="ansible.build"]')) {
    return
  }
  var script = document.createElement('script')
  script.defer = true
  script.dataset.domain = 'ansible.build'
  script.src = 'https://plausible.io/js/script.js'
  document.head.appendChild(script)
})()
