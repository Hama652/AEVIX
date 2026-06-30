import { NavLink } from 'react-router-dom'
import { navigationItems } from '../../lib/navigation'

export function Sidebar() {
  return (
    <aside className="sidebar">
      <div className="sidebar__brand">
        <div className="sidebar__mark">A</div>
        <div>
          <div className="sidebar__title">AEVIX</div>
          <div className="sidebar__subtitle">Dashboard Shell</div>
        </div>
      </div>

      <nav className="sidebar__nav" aria-label="Primary">
        {navigationItems.map((item) => (
          <NavLink
            key={item.key}
            to={item.path}
            end={item.path === '/'}
            className={({ isActive }) => `sidebar__link${isActive ? ' sidebar__link--active' : ''}`}
          >
            <span className="sidebar__link-label">{item.label}</span>
            <span className="sidebar__link-description">{item.description}</span>
          </NavLink>
        ))}
      </nav>
    </aside>
  )
}
