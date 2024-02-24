<script>
    import { onMount } from 'svelte';
    let names = [];
    let newName = '';
  
    onMount(async () => {
      const response = await fetch('http://localhost:8000/names');
      const data = await response.json();
      names = data.names;
    });
  
    async function handleSubmit() {
      const response = await fetch('http://localhost:8000/names', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ name: newName })
      });
      const data = await response.json();
      names = data.names;
      newName = ''; // Clear the input after submission
    }
  </script>
  
  <h1>Names List</h1>
  <form on:submit|preventDefault={handleSubmit}>
    <input bind:value={newName} placeholder="Enter your name" />
    <button type="submit">Submit</button>
  </form>
  
  <ul>
    {#each names as name}
      <li>{name}</li>
    {/each}
  </ul>
  