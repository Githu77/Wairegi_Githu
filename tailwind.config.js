/** @type {import('tailwindcss').Config} */
module.exports = {
  darkMode: 'class',
  content: [
    './WairegiG/GithuApp/templates/**/*.html', 
    '.WairegiG/GithuApp/static/js/**/*.js'
  ],
  theme: {
    extend: {
      colors: {
        myGrey: {
          DEFAULT: '#D9D0C1',
        },
        DarkBlue: {
          DEFAULT: '#1E2640',
          light: '#393F60',
          dark: '#0D1228',
        },
        myBiege: {
          DEFAULT: '#033859',
        },
        myGreen: {
          DEFAULT: '#072A40',
        },
      },
    },
  },
  plugins: [],
}
