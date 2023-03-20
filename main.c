#include <gtk/gtk.h>


void on_download_click(GtkButton *btn, gpointer user_data) {

    GtkEntry *link_entry;
    const gchar *link;
    GString *command;

    link_entry = user_data;
    link = gtk_entry_get_text(link_entry);
    command = g_string_append(g_string_new("yt-dlp "), link);

    system(command->str);
    
}




void activate(GtkApplication *app, gpointer user_data) {

    GtkBuilder *builder;
    GtkWidget *window;
    GtkWidget *btn;
    GtkWidget *entry;
    
    builder = gtk_builder_new_from_file("ui.glade");
    window = GTK_WIDGET(gtk_builder_get_object(builder, "main_window"));
    btn = GTK_WIDGET(gtk_builder_get_object(builder, "download_button"));
    entry = GTK_WIDGET(gtk_builder_get_object(builder, "link_entry"));

    gtk_window_set_application(GTK_WINDOW(window), GTK_APPLICATION(app));

    g_signal_connect(btn, "clicked", G_CALLBACK(on_download_click), entry);

    gtk_window_present(GTK_WINDOW(window));

    g_object_unref(builder);

}



int main(int argc, char** argv) {
    
    GtkApplication *app;
    int status;

    app = gtk_application_new("com.github.EnderNight.yt_dlp_gui", G_APPLICATION_DEFAULT_FLAGS);

    g_signal_connect(app, "activate", G_CALLBACK(activate), NULL);

    status = g_application_run(G_APPLICATION(app), argc, argv);

    g_object_unref(app);

    return status;

}
