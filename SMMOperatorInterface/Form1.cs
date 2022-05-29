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
                News news = new News();
                while ((line = reader.ReadLine()) != null) {
                    if (line == " ") {
                        if (news != null) {
                            ListCustomer.Add(news);
                            news = new News {
                                HashTag = "#от_заказчика"
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
            for (int i = 0; i < checkedListBox.CheckedItems.Count; i++) {
                news1 = checkedListBox.CheckedItems[i] as News;
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