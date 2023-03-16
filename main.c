#include <gtk/gtk.h>


void activate(GtkApplication *app, gpointer user_data) {

    printf("activate called\n");

    GtkBuilder *builder;
    GObject *window;
    
    builder = gtk_builder_new_from_file("ui.glade");
    window = gtk_builder_get_object(builder, "main_window");

    gtk_window_present(GTK_WINDOW(window));

    g_object_unref(builder);

}



int main(int argc, char** argv) {
    
    GtkApplication *app;
    int status;

    app = gtk_application_new("org.yt_dlp_gui", G_APPLICATION_DEFAULT_FLAGS);

    g_signal_connect(app, "activate", G_CALLBACK(activate), NULL);

    status = g_application_run(G_APPLICATION(app), argc, argv);

    g_object_unref(app);

    return status;

}
