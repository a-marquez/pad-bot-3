<script lang="ts">
  import { dev } from '$app/environment';
  import { onMount } from 'svelte'
  let deviceSerials: string[] = []
  let selectedDeviceSerial: string;
  let api: object;

  onMount(async () => {
    api = pywebview.api
    deviceSerials = await api.get_device_serials()
    selectedDeviceSerial = deviceSerials[0]
  })

  async function debug() {
    console.log('debug')
  }
</script>

<h1>Debug</h1>

<div>
  <label for="select">Device: </label>
  <select bind:value={selectedDeviceSerial}>
    {#each deviceSerials as serial}
      <option>{serial}</option>
    {/each}
  </select>
</div>

<br />

<div>
  <button on:click={debug}>debug</button>
  <button on:click={() => api.toggle_device_screen(selectedDeviceSerial)}>Toggle screen</button>
  <button on:click={() => api.multi_point_swipe(selectedDeviceSerial)}>Multi-point Swipe</button>
</div>
