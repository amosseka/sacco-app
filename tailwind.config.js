module.exports = {
  content: [
    './templates/*{.html,js}',
    './main/**/*.{html,js}'
  ],
  theme: {
    extend: {
      colors: {
        tooltip: "#555",
        formbg: "#FAFCFE",
        navlink: "#424A59",
        bluish: "#E8EEF6",
        "row-odd": "#FBFBFB",
        "row-even": "#F4F4F6",
        "dark-heading": "#353535",
        "darker-heading": "#161D22",
        "select-bg": "#EDEDED",
        "input-border": "#DEDEDE",
      }
    },
  },
  plugins: [],
}
