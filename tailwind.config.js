export const content = [
    './templates/*{.html,js}',
    './main/**/*.{html,js}',
    './accounts/**/*.{html,js}',
];
export const theme = {
    extend: {
        borderColor: {
            DEFAULT: 'rgb(229 231 235)',
        },
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
        },
    },
};
export const plugins = [];
