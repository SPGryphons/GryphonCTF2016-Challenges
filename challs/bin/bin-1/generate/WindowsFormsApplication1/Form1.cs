using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace WindowsFormsApplication1
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
        }

        private void button1_Click(object sender, EventArgs e)
        {
            string password = "I guess it's not gonna be so easy? or is it?";
            if (textBox1.Text == password)
               MessageBox.Show("GCTF{pl5_53cur3_y0ur_d07_n37}");
            else
            {
                MessageBox.Show("Try harder. Even that gorilla can solve this question");
            }
        }
    }
}
