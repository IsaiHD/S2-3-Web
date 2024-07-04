import { NavItem } from './nav-item/nav-item';

export const navItems: NavItem[] = [
  {
    navCap: 'Home',
  },
  {
    displayName: 'Dashboard',
    iconName: 'layout-dashboard',
    route: '/dashboard',
  },
  {
    displayName: 'Saludo',
    iconName: 'message',
    route: '/greeting',
  },
  {
    displayName: 'Chat',
    iconName: 'chat',
    route: '/chat',  // Asegúrate de que esta ruta esté configurada correctamente en tu enrutador
  },
];
