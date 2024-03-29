namespace SMMOperatorInterface {
    public partial class Form1 : Form {
        List<News> ListNews = new List<News>();
        List<News> ListCustomer = new List<News>();
        public Form1() {
            InitializeComponent();
        }
        private void Form1_Load(object sender, EventArgs e) {
            GetNews("news_input.txt");
            GetCustomerInfo("customer_input.txt");
        }

        private void GetNews(string path) {
            using (StreamReader reader = new StreamReader(path)) {
                string? line;
                int flag = 0;
                News news = new News();
                while ((line = reader.ReadLine()) != null) {
                    if (line == " ") {
                        flag = 0;
                        if (news != null) {
                            ListNews.Add(news);
                            news = new News();
                        }
                    } else if (flag == 0) {
                        flag++;
                        news.Title = line;
                    } else if (flag == 1) {
                        flag++;
                        news.Href = line;
                    } else if (flag == 2) {
                        news.HashTag = line;
                    }
                }
                if (reader.EndOfStream) {
                    if (news != null) {
                        ListNews.Add(news);
                    }
                }
            }
            checkedListBox1.Items.AddRange(ListNews.ToArray());
        }

        private void GetCustomerInfo(string path) {
            using (StreamReader reader = new StreamReader(path)) {
                string? line;
                int flag = 0;
                News news = new News() {
                    HashTag = "#��_���������"
                };
                while ((line = reader.ReadLine()) != null) {
                    if (line == " ") {
                        if (news != null) {
                            ListCustomer.Add(news);
                            news = new News {
                                HashTag = "#��_���������"
                            };
                        }
                    } else {
                        flag++;
                        news.Title = line;
                    }
                }
                if (reader.EndOfStream) {
                    if (news != null) {
                        ListCustomer.Add(news);
                    }
                }
            }
            checkedListBox2.Items.AddRange(ListCustomer.ToArray());
        }

        private void checkedListBox1_ItemCheck(object sender, ItemCheckEventArgs e) {
            rtbPublic.Clear();
            CheckedListBox checkedListBox = (CheckedListBox)sender;
            News news1;
            for (int i = 0; i < checkedListBox1.CheckedItems.Count; i++) {
                news1 = checkedListBox1.CheckedItems[i] as News;
                if (news1 == null) continue;
                rtbPublic.Text += news1.Title + "\n" + (news1.Href != "" ? news1.Href + "\n" : "") + news1.HashTag + "\n\n";
            }
            for (int i = 0; i < checkedListBox2.CheckedItems.Count; i++) {
                news1 = checkedListBox2.CheckedItems[i] as News;
                if (news1 == null) continue;
                rtbPublic.Text += news1.Title + "\n" + (news1.Href != "" ? news1.Href + "\n" : "") + news1.HashTag + "\n\n";
            }
            if (e.NewValue == CheckState.Checked) {
                if (tabControl.SelectedTab == tabControl.TabPages[1]) {
                    news1 = ListCustomer[e.Index];
                } else {
                    news1 = ListNews[e.Index];
                }
                rtbPublic.Text += news1.Title + "\n" + (news1.Href != "" ? news1.Href + "\n" : "") + news1.HashTag + "\n\n";
            }
        }

        private void fileSystemWatcher1_Changed(object sender, FileSystemEventArgs e) {
            ListCustomer.Clear();
            ListNews.Clear();
            checkedListBox1.Items.Clear();
            checkedListBox2.Items.Clear();
            rtbPublic.Text = "";
            GetCustomerInfo("customer_input.txt");
            GetNews("news_input.txt");
            this.Refresh();
        }

        private void button1_Click(object sender, EventArgs e) {
            System.Diagnostics.Process.Start("python", "getlink.py");
        }
    }

    public class News {
        public string Title { get; set; } = "";
        public string Href { get; set; } = "";
        public string HashTag { get; set; } = "";
        public News() { }
        public override string ToString() {
            return Title;
        }
    }
}