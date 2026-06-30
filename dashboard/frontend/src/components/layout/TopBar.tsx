export function TopBar() {
  return (
    <header className="topbar">
      <div>
        <div className="topbar__eyebrow">AEVIX Operations</div>
        <h1 className="topbar__title">Research Control Plane</h1>
      </div>
      <div className="topbar__status" aria-label="Dashboard status">
        Dashboard shell ready
      </div>
    </header>
  )
}
