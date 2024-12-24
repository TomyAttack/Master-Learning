<?php

use Illuminate\Support\Facades\Route;

Route::get('/', function () {
    return view('welcome');
});

// Route::get('home', 'HomesController@index');
Route::get('home', 'Dashboard\HomesController@index');
// Route::get('home', 'Dashboard/HomesController@index');
// Route::get('home', 'App\Http\Dashboard\HomesController@index');
// Route::get('home', [HomesController::class,'index']);
// Route::get(
//     'home',
//     [App\Http\Dashboard\HomeController::class, 'show']
// )->name('home');
// Route::get('home', function ()
// {
//     return "ini home";
// });