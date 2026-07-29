<script setup>
import ParentLayout from '@vuepress/theme-default/layouts/Layout.vue'
</script>

<template>
  <ParentLayout>
    <template #navbar-before>
      <a href="https://www.mint-system.ch/" target="_blank" rel="noopener noreferrer" class="mint-system-brand">Mint System GmbH</a>
    </template>
  </ParentLayout>
</template>

<style lang="css">
.mint-system-brand {
  display: inline-flex;
  align-items: center;
  margin-right: 1rem;
  padding: 0.35rem 0.9rem;
  border-radius: 6px;
  background-color: #14d6c4;
  color: #fff;
  font-weight: 600;
  font-size: 0.9rem;
  text-decoration: none;
  white-space: nowrap;
}
.mint-system-brand:hover {
  background-color: #0B9FA3;
  color: #fff;
}
</style>