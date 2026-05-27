/** @type {import('tailwindcss').Config} */
export default {
  content: ['./index.html', './src/**/*.{js,ts,jsx,tsx}'],
  theme: {
    extend: {
      colors: {
        primary:  { DEFAULT: '#1A3557', light: '#2E6DA4', pale: '#D6E4F0' },
        accent:   { DEFAULT: '#C8960C' },
        surface:  { DEFAULT: '#F8FAFC', card: '#FFFFFF' },
      },
      fontFamily: {
        sans: ['Inter', 'system-ui', 'sans-serif'],
        display: ['Plus Jakarta Sans', 'sans-serif'],
      }
    }
  },
  plugins: []
}
