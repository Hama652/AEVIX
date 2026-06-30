export type DashboardRouteKey =
  | 'dashboard'
  | 'training'
  | 'models'
  | 'datasets'
  | 'experiments'
  | 'checkpoints'
  | 'cloud'
  | 'settings'
  | 'logs'
  | 'about'

export interface NavigationItem {
  key: DashboardRouteKey
  label: string
  path: string
  description: string
}

export const navigationItems: NavigationItem[] = [
  { key: 'dashboard', label: 'Dashboard', path: '/', description: 'Operational overview' },
  { key: 'training', label: 'Training', path: '/training', description: 'Job control surface' },
  { key: 'models', label: 'Models', path: '/models', description: 'Model catalog' },
  { key: 'datasets', label: 'Datasets', path: '/datasets', description: 'Upload and governance' },
  { key: 'experiments', label: 'Experiments', path: '/experiments', description: 'Tracking and comparison' },
  { key: 'checkpoints', label: 'Checkpoints', path: '/checkpoints', description: 'Artifacts and recovery' },
  { key: 'cloud', label: 'Cloud', path: '/cloud', description: 'GPU and provider status' },
  { key: 'settings', label: 'Settings', path: '/settings', description: 'Workspace configuration' },
  { key: 'logs', label: 'Logs', path: '/logs', description: 'Live operational output' },
  { key: 'about', label: 'About', path: '/about', description: 'Platform context' },
]
