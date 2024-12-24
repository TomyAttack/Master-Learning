<?php

namespace App\Providers;

use Illuminate\Support\ServiceProvider;
use Illuminate\Support\Facades\Route;
class RouteServiceProvider extends ServiceProvider
{
    protected $namespace = 'App\Http\Controllers';
    /**
     * Register services.
     */
    public function register(): void
    {
        //
    }

    /**
     * Bootstrap services.
     */
    public function boot(): void
    {
        //

        // parent::boot();
        $this->mapWebRoutes();
    }

    public function map()
    {
        // $this->mapApiRoutes();

        $this->mapWebRoutes();

        //
    }

     protected function mapWebRoutes()
    {
        Route::middleware('web')
             ->namespace($this->namespace)
             ->group(base_path('routes/web.php'));
    }

}
