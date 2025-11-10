export { COOKIE_NAME, ONE_YEAR_MS } from "@shared/const";

export const APP_TITLE = import.meta.env.VITE_APP_TITLE || "App";

export const APP_LOGO = "https://placehold.co/128x128/E1E7EF/1F2937?text=App";

// Generate login URL at runtime so redirect URI reflects the current origin.
export const getLoginUrl = () => {
  const oauthPortalUrl = import.meta.env.VITE_OAUTH_PORTAL_URL;
  const appId = import.meta.env.VITE_APP_ID;
  const redirectUri = `${window.location.origin}/api/oauth/callback`;
  const state = btoa(redirectUri);

  const url = new URL(`${oauthPortalUrl}/app-auth`);
  url.searchParams.set("appId", appId);
  url.searchParams.set("redirectUri", redirectUri);
  url.searchParams.set("state", state);
  url.searchParams.set("type", "signIn");

  return url.toString();
};

export const UTTERANCES_REPO =
  import.meta.env.VITE_UTTERANCES_REPO || "CaldeIsa/catalogo-pinturas-comentarios";

export const UTTERANCES_ISSUE_TERM =
  import.meta.env.VITE_UTTERANCES_ISSUE_TERM || "pathname";

export const UTTERANCES_LABEL = import.meta.env.VITE_UTTERANCES_LABEL?.trim() || undefined;

export const UTTERANCES_THEME =
  import.meta.env.VITE_UTTERANCES_THEME || "github-light";
